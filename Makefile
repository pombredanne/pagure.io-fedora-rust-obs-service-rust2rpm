PREFIX=/usr
LOCALSTATEDIR=/var

OBS_SERVICE_DIR=$(PREFIX)/lib/obs/service
OBS_SERVICE_CACHE_DIR=$(LOCALSTATEDIR)/cache/obs

all:

install:
	install -d $(DESTDIR)$(OBS_SERVICE_DIR)
	install -pm 0755 obs-rust2rpm.py $(DESTDIR)$(OBS_SERVICE_DIR)/rust2rpm
	install -pm 0644 obs-rust2rpm.service $(DESTDIR)$(OBS_SERVICE_DIR)/rust2rpm.service
	install -d $(DESTDIR)$(OBS_SERVICE_CACHE_DIR)/rust2rpm

