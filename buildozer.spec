[app]

title = My Notes
package.name = mynotes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3==3.11.0, kivy, plyer

icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, VIBRATE, BODY_SENSORS

android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

android.gradle_dependencies = ''
android.add_src = 

android.ignore_manifest_merged = True

android.gradle_task = assembleDebug
android.gradle_offline = False

android.java_version = 11

android.ndk_cache = True

log_level = 2

downloader_timeout = 60

android.override_apk_name = True

[buildozer]

log_level = 2
