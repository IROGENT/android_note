[app]

title = My Notes
package.name = mynotes
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1
version.code = 1

requirements = python3,kivy==2.3.1,kivymd==2.0.1,plyer

icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_FINE_LOCATION

android.gradle_dependencies = com.google.android.gms:play-services-location:21.0.1

android.api = 30
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license = True

android.archs = arm64-v8a

android.debug = 1

log_level = 2

[buildozer]

log_level = 2
