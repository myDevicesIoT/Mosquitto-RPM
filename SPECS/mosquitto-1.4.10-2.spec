Summary: Mosquitto Broker build
Name: mosquitto
Version: 1.4.10
Release: 2
License: GPL
Group: System Environment/Base
Source: https://github.com/myDevicesIoT/mosquitto/archive/v1.4.10.tar.gz
Patch0: mosquitto-disconnect-notification.patch
Source1: init.tar.gz

BuildRequires: openssl-devel cmake c-ares-devel libuuid-devel

%description
Mosquitto MQTT Broker

%prep
%setup -q
%patch0 -p1 -b .buildroot
%setup -T -D -a 1

%build
make WITH_WEBSOCKETS=yes RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR="$RPM_BUILD_ROOT" prefix=/usr
mkdir -p "$RPM_BUILD_ROOT/etc/init.d"
cp init/mosquitto "$RPM_BUILD_ROOT/etc/init.d/"

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/libmosquitto.so.1
/usr/lib/libmosquitto.so
/usr/include/mosquitto.h
/usr/lib/libmosquittopp.so.1
/usr/lib/libmosquittopp.so
/usr/include/mosquittopp.h
/usr/bin/mosquitto_pub
/usr/bin/mosquitto_sub
/usr/sbin/mosquitto
/usr/include/mosquitto_plugin.h
/usr/bin/mosquitto_passwd
/etc/init.d/mosquitto
/etc/mosquitto/aclfile.example
/etc/mosquitto/mosquitto.conf.example
/etc/mosquitto/pskfile.example
/etc/mosquitto/pwfile.example

%post -p /sbin/ldconfig
%preun
/sbin/service mosquitto stop
/sbin/chkconfig --del mosquitto

%postun -p /sbin/ldconfig

%changelog
* Fri Dec 30 2016 Leszek Eljasz <leljasz@mydevices.com>
- Compile with websocket support

* Tue Sep 6 2016 David Achenbach <dachenbach@mydevices.com>
- Patch added to notify on disconnect

* Tue Sep 6 2016 David Achenbach <dachenbach@mydevices.com>
- RPM build directly from mosquitto 1.4.10 source
