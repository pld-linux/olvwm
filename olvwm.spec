Summary:	OpenLook Virtual Window Manager.
Name:		olvwm
Version:	4.2n
Release:	1
License:	GPL
Vendor:		JaeSub Hong
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	%{name}.%{version}.src.tar.gz
URL:		http://www.phys.columbia.edu/~flame/olvwm.html
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	olgx

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Olvwm (OPEN LOOK virtual window manager) is an ICCCM compliant window
manager supplied for use with the XView toolkit. It is derived from
olwm, the OPEN LOOK window manager supplied with the XView release.
This version of olvwm is based on version 3 of the XView release.

OpenLook was also look and feel style used on older Sun workstation,
before Sun discontinued it and started using CDE. Even as new window
managers emerged some - especially Unix veterans - stick to the olvwm
as it reminds them of good, old days when they were young hackers...

%prep
%setup -q -n olvwm.4.2n

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/local/openwin/{bin,lib/help}
install -d $RPM_BUILD_ROOT%{_prefix}/local/man/man{1,5}
install olvwm $RPM_BUILD_ROOT%{_prefix}/local/openwin/bin
install olvwm.info $RPM_BUILD_ROOT%{_prefix}/local/openwin/lib/help
cp olvwmrc.man olvwmrc.5
cp olwm.man olvwm.1
install olvwm.1 $RPM_BUILD_ROOT%{_prefix}/local/man/man1
install olvwmrc.5 $RPM_BUILD_ROOT%{_prefix}/local/man/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LEGAL_NOTICE NEW_CHANGES CHANGES
%attr(644,root,man) %{_prefix}/local/man/man1/olvwm.1
%attr(644,root,man) %{_prefix}/local/man/man5/olvwmrc.5
%{_prefix}/local/openwin/bin/olvwm
%attr(644,root,root) %{_prefix}/local/openwin/lib/help/olvwm.info
