PREFIX=/usr

all:
	@echo "You can run Anki with ./runanki"
	@echo "If you wish to install it system wide, type 'sudo make install'"
	@echo "Uninstall with 'sudo make uninstall'"

install:
	rm -rf ${DESTDIR}${PREFIX}/share/anki
	mkdir -p ${DESTDIR}${PREFIX}/share/anki
	cp -av anki aqt web ${DESTDIR}${PREFIX}/share/anki/
	-cp -av locale ${DESTDIR}${PREFIX}/share/anki/
	sed -e 's:@PREFIX@:${PREFIX}:' tools/runanki.system.in > tools/runanki.system
	install -m 0755 -D tools/runanki.system ${DESTDIR}${PREFIX}/bin/anki
	install -m 0644 -D -t ${DESTDIR}${PREFIX}/share/pixmaps anki.xpm anki.png
	install -m 0644 -D -t ${DESTDIR}${PREFIX}/share/applications anki.desktop
	install -m 0644 -D -t ${DESTDIR}${PREFIX}/share/man/man1 anki.1
	install -m 0644 -D -t ${DESTDIR}${PREFIX}/share/doc/anki README.contributing README.development README.md LICENSE LICENSE.logo
	-xdg-mime install anki.xml --novendor
	-xdg-mime default anki.desktop application/x-anki
	-xdg-mime default anki.desktop application/x-apkg
	@echo
	@echo "Install complete."

uninstall:
	rm -rf ${DESTDIR}${PREFIX}/share/anki
	rm -rf ${DESTDIR}${PREFIX}/bin/anki
	rm -rf ${DESTDIR}${PREFIX}/share/pixmaps/anki.xpm
	rm -rf ${DESTDIR}${PREFIX}/share/pixmaps/anki.png
	rm -rf ${DESTDIR}${PREFIX}/share/applications/anki.desktop
	rm -rf ${DESTDIR}${PREFIX}/share/man/man1/anki.1
	-xdg-mime uninstall ${DESTDIR}${PREFIX}/share/mime/packages/anki.xml
	@echo
	@echo "Uninstall complete."

MAKEFLAGS += --silent

ANKI_BASE_FOLDER ?= ankirun
ANKI_PROFILE     ?= User 1
ANKI_LANG        ?= en_US


.PHONY: build_python
build_python:
	./configure --with-openssl=$(brew --prefix openssl@1.1) CPPFLAGS="-I$(brew --prefix sqlite)/include" LDFLAGS="-L$(brew --prefix sqlite)/lib"
	make
	./python.exe -c 'import sqlite3; print(sqlite3.sqlite_version)'
	sqlite3 --version


.PHONY: install_python_through_pyenv
install_python_through_pyenv:
	export CPPFLAGS="$$CPPFLAGS -I/usr/local/opt/sqlite/include"
	export LIBSQLITE3_CFLAGS='-I/usr/local/opt/sqlite/include'

	export LDFLAGS="$$LDFLAGS -L/usr/local/opt/sqlite/lib"
	export LIBSQLITE3_LIBS='-L/usr/local/opt/sqlite/lib'

	pyenv install 3.9.13

.PHONY: run
run:
	./runanki --base "$(ANKI_BASE_FOLDER)" --profile "$(ANKI_PROFILE)" --lang "$(ANKI_LANG)"

.PHONY: db_shell
db_shell:
	echo "$(ANKI_BASE_FOLDER)/$(ANKI_PROFILE)/collection.anki2"
	sqlite3 "$(ANKI_BASE_FOLDER)/$(ANKI_PROFILE)/collection.anki2"

.PHONY: clear
clear:
	rm -rf "$(ANKI_BASE_FOLDER)"
	echo 'anki base folder removed'
