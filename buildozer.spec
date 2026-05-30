[app]

title = My Notes
package.name = mynotes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1
version.code = 1

requirements = python3,kivy,kivymd,plyer,android

icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_FINE_LOCATION

android.api = 30
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license = True

android.archs = arm64-v8a

log_level = 2

[buildozer]

log_level = 2
