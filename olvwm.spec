Summary: OpenLook Virtual Window Manager.
Name: olvwm
Version: 4.2n
Release: 1
Copyright: GPL
Vendor: JaeSub Hong
packager: Andy C. Brandt <andy@uranos.eu.org>
Group: User Interface/X
Source: olvwm.4.2n.src.tar.gz
URL: http://www.phys.columbia.edu/~flame/olvwm.html
Buildroot: %{_tmppath}/%{name}-root
Requires: olgx

%description
Olvwm (OPEN LOOK virtual window manager) is an ICCCM compliant window manager
supplied for use with the XView toolkit.  It is derived from olwm, the
OPEN LOOK window manager supplied with the XView release.  This version of
olvwm is based on version 3 of the XView release.

OpenLook was also look and feel style used on older Sun workstation, before Sun
discontinued it and started using CDE.  Even as new window managers emerged
some - especially Unix veterans - stick to the olvwm as it reminds them of
good, old days when they were young hackers...

%prep
%setup -n olvwm.4.2n

%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/local/openwin/{bin,lib/help}
install -d $RPM_BUILD_ROOT/usr/local/man/man{1,5}
install olvwm $RPM_BUILD_ROOT/usr/local/openwin/bin
install -m 644 olvwm.info $RPM_BUILD_ROOT/usr/local/openwin/lib/help
cp olvwmrc.man olvwmrc.5
cp olwm.man olvwm.1
install -m 644 olvwm.1 $RPM_BUILD_ROOT/usr/local/man/man1
install -m 644 olvwmrc.5 $RPM_BUILD_ROOT/usr/local/man/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LEGAL_NOTICE NEW_CHANGES CHANGES
%attr(644,root,man)	/usr/local/man/man1/olvwm.1
%attr(644,root,man)	/usr/local/man/man5/olvwmrc.5
/usr/local/openwin/bin/olvwm
%attr(644,root,root)	/usr/local/openwin/lib/help/olvwm.info

%changelog
* Thu Aug 24 2000 Andy C. Brandt <andy@uranos.eu.org>
- created this package from sources
