Summary:	OpenLook Virtual Window Manager
Summary(pl):	OpenLook Virtual Window Manager - Wirtualny Zarz�dca Okien
Name:		olvwm
Version:	4.2n
Release:	1
License:	some BSD-like (see LEGAL_NOTICE)
Vendor:		JaeSub Hong
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fen�tres
Group(pl):	X11/Zarz�dcy Okien
Source0:	http://www.phys.columbia.edu/~flame/files/%{name}.%{version}.src.tar.gz
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

%description -l pl
Olvwm (OPEN LOOK virtual window manager) jest zgodnym z ICCCM zarz�dc�
okien przeznaczonym do toolkitu XView. Wywodzi si� z olwm (OPEN LOOK
window manager) dostarczanego wraz z XView. Ta wersja olvwm bazuje na
wersji 3 XView.

OpenLook by� stylem u�ywanym na starszych stacjach Suna, zanim Sun
wycofa� si� z niego i zacz�� u�ywa� CDE. Szczeg�lmnie uniksowi
weterani ch�tnie pozostaj� przy olvwm jako �e przypomina im stare, dobre
czasy, kiedy byli m�odymi hackerami...

%prep
%setup -q -n %{name}.%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}
install olvwm $RPM_BUILD_ROOT%{_bindir}
install olwm.man $RPM_BUILD_ROOT%{_mandir}/man1/olvwm.1
install olvwmrc.man $RPM_BUILD_ROOT%{_mandir}/man5/olvwmrc.5

gzip -9nf README LEGAL_NOTICE NEW_CHANGES CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz olvwm.info
%{_mandir}/man[15]/*
%attr(755,root,root) %{_bindir}/olvwm
%{_prefix}/local/openwin/lib/help/olvwm.info
