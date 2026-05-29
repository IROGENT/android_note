[app]

title = My Notes
package.name = mynotes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3,kivy==2.2.0,plyer,android

icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, VIBRATE, BODY_SENSORS

android.api = 30
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
