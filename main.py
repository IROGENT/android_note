from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from database import init_database, add_note, get_all_notes, delete_note, update_note, get_note_by_id
from kivy.uix.floatlayout import FloatLayout
from plyer import accelerometer
from kivy.clock import Clock


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = FloatLayout()

        list_layout = MDBoxLayout(orientation='vertical', spacing=5, padding=15)

        up_panel = MDTopAppBar(title='Заметки', md_bg_color='brown')
        list_layout.add_widget(up_panel)

        scroll = ScrollView()
        list_layout.add_widget(scroll)

        self.notes_list = MDList()
        scroll.add_widget(self.notes_list)

        main_layout.add_widget(list_layout)

        action_button = MDIconButton(
            icon='plus',
            font_size="56sp",
            pos_hint={"right": 0.93, "y": 0.04},
            theme_icon_color="Custom",
            icon_color=(0, 0, 1, 1),
            on_release=self.open_new_note
        )
        main_layout.add_widget(action_button)

        self.add_widget(main_layout)
        self.load_notes()

    def load_notes(self):
        self.notes_list.clear_widgets()
        all_notes = get_all_notes()
        for note in all_notes:
            item = TwoLineListItem(
                text=note[1],
                secondary_text=note[3],
                on_release=lambda x, n=note: self.open_note(n)
            )
            self.notes_list.add_widget(item)

    def open_note(self, note):
        self.manager.current = 'note'
        self.manager.get_screen('note').set_note_id(note[0])

    def open_new_note(self, instance):
        self.manager.current = 'note'
        self.manager.get_screen('note').set_note_id(None)


class MainApp(MDApp):
    def build(self):
        init_database()
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NoteScreen(name='note'))

        self.start_accelerometer()

        return sm

    def start_accelerometer(self):
        try:
            accelerometer.enable()
            Clock.schedule_interval(self.check_shake, 0.1)
        except Exception as e:
            print(f"Акселерометр не поддерживается: {e}")

    def check_shake(self, dt):
        try:
            val = accelerometer.acceleration[:3]
            x, y, z = abs(val[0]), abs(val[1]), abs(val[2])

            if x + y + z > 30:
                self.show_shake_dialog()
                Clock.unschedule(self.check_shake)
                Clock.schedule_once(lambda dt: self.start_accelerometer(), 3)
        except Exception:
            pass

    def show_shake_dialog(self):
        dialog = MDDialog(
            title="Землетрясение",
            text="Причина тряски?",
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()


class NoteScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.note_id = None
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=20)

        self.toolbar = MDTopAppBar(
            title="Новая заметка",
            md_bg_color='brown',
            left_action_items=[["arrow-left", lambda x: self.go_back()]]
        )
        layout.add_widget(self.toolbar)

        self.title_field = MDTextField(
            hint_text="Заголовок",
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.title_field)

        self.content_field = MDTextField(
            hint_text="Содержание заметки",
            multiline=True,
            size_hint_y=0.6
        )
        layout.add_widget(self.content_field)

        buttons_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=10,
            size_hint_y=None,
            height=50
        )
        save_button = MDRectangleFlatButton(
            text="Сохранить",
            on_release=self.save_note
        )
        delete_button = MDRectangleFlatButton(
            text="Удалить",
            on_release=self.confirm_delete
        )
        buttons_layout.add_widget(save_button)
        buttons_layout.add_widget(delete_button)
        layout.add_widget(buttons_layout)

        self.add_widget(layout)

    def set_note_id(self, note_id):
        self.note_id = note_id
        if note_id is not None:
            self.toolbar.title = "Редактировать заметку"
            note = get_note_by_id(note_id)
            if note:
                self.title_field.text = note[1]
                self.content_field.text = note[2]
        else:
            self.title_field.text = ""
            self.content_field.text = ""

    def save_note(self, instance):
        title = self.title_field.text.strip()
        content = self.content_field.text.strip()

        if not title:
            title = "Без названия"

        if self.note_id is None:
            add_note(title, content)
        else:
            update_note(self.note_id, title, content)

        self.go_back()

    def confirm_delete(self, instance):
        if self.note_id is None:
            self.go_back()
            return

        self.dialog = MDDialog(
            title="Удалить заметку?",
            text="Это действие нельзя отменить.",
            buttons=[
                MDFlatButton(text="Отмена", on_release=lambda x: self.dialog.dismiss()),
                MDRectangleFlatButton(text="Удалить", on_release=lambda x: self.delete_current_note())
            ]
        )
        self.dialog.open()

    def delete_current_note(self):
        if self.note_id:
            delete_note(self.note_id)
        self.dialog.dismiss()
        self.go_back()

    def go_back(self):
        self.manager.current = 'main'
        self.manager.get_screen('main').load_notes()
        self.title_field.text = ""
        self.content_field.text = ""
        self.note_id = None
        self.toolbar.title = "Новая заметка"


if __name__ == '__main__':
    MainApp().run()
