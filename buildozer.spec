[app]

title = My Notes
package.name = mynotes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3==3.11.0, kivy

icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 30
android.minapi = 21
android.ndk = 23c
android.accept_sdk_license = True

android.archs = arm64-v8a

log_level = 2

[buildozer]

log_level = 2
