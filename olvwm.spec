#
# TODO:
# - add desktop file.
#
Summary:	OpenLook Virtual Window Manager
Summary(pl):	OpenLook Virtual Window Manager - Wirtualny Zarz±dca Okien
Name:		olvwm
Version:	4.2n
Release:	4
License:	BSD-like (see LEGAL_NOTICE)
Vendor:		JaeSub Hong
Group:		X11/Window Managers
Source0:	http://www.phys.columbia.edu/~flame/files/%{name}.%{version}.src.tar.gz
Source1:	%{name}-config.examples.tar.bz2
Source2:	%{name}.desktop
Patch0:		%{name}-pld.patch
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imake
BuildRequires:	xview
BuildRequires:	xview-devel
URL:		http://www.phys.columbia.edu/~flame/olvwm.html
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	%{_datadir}/wm-properties

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
Olvwm (OPEN LOOK virtual window manager) jest zgodnym z ICCCM zarz±dc±
okien przeznaczonym do toolkitu XView. Wywodzi siê z olwm (OPEN LOOK
window manager) dostarczanego wraz z XView. Ta wersja olvwm bazuje na
wersji 3 XView.

OpenLook by³ stylem u¿ywanym na starszych stacjach Suna, zanim Sun
wycofa³ siê z niego i zacz±³ u¿ywaæ CDE. Szczególmnie uniksowi
weterani chêtnie pozostaj± przy olvwm jako ¿e przypomina im stare,
dobre czasy, kiedy byli m³odymi hackerami...

%prep
%setup -q -n %{name}.%{version} -a 1
%patch0 -p1

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_wmpropsdir}}

install olvwm $RPM_BUILD_ROOT%{_bindir}
install olwm.man $RPM_BUILD_ROOT%{_mandir}/man1/olwm.1
install olvwm.man $RPM_BUILD_ROOT%{_mandir}/man1/olvwm.1
install olvwmrc.man $RPM_BUILD_ROOT%{_mandir}/man5/olvwmrc.5

install %{SOURCE2} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LEGAL_NOTICE NEW_CHANGES CHANGES olvwm.info
%doc %dir config.examples
%{_mandir}/man[15]/*
%attr(755,root,root) %{_bindir}/olvwm
%{_wmpropsdir}/%{name}.desktop
