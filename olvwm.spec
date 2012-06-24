#
# TODO:
# - add desktop file.
#
Summary:	OpenLook Virtual Window Manager
Summary(pl.UTF-8):	OpenLook Virtual Window Manager - Wirtualny Zarządca Okien
Name:		olvwm
Version:	4.2n
Release:	4
License:	BSD-like (see LEGAL_NOTICE)
Group:		X11/Window Managers
Source0:	http://www.phys.columbia.edu/~flame/files/%{name}.%{version}.src.tar.gz
# Source0-md5:	21aeb96b94d7cce8ce3dcff13d34716a
Source1:	%{name}-config.examples.tar.bz2
# Source1-md5:	bdde57ef48ccc802b62ec510ab14aee2
Source2:	%{name}.desktop
Source3:	%{name}-xsession.desktop
Patch0:		%{name}-pld.patch
URL:		http://www.phys.columbia.edu/~flame/olvwm.html
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imake
BuildRequires:	xview
BuildRequires:	xview-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Olvwm (OPEN LOOK virtual window manager) is an ICCCM compliant window
manager supplied for use with the XView toolkit. It is derived from
olwm, the OPEN LOOK window manager supplied with the XView release.
This version of olvwm is based on version 3 of the XView release.

OpenLook was also look and feel style used on older Sun workstation,
before Sun discontinued it and started using CDE. Even as new window
managers emerged some - especially Unix veterans - stick to the olvwm
as it reminds them of good, old days when they were young hackers...

%description -l pl.UTF-8
Olvwm (OPEN LOOK virtual window manager) jest zgodnym z ICCCM zarządcą
okien przeznaczonym do toolkitu XView. Wywodzi się z olwm (OPEN LOOK
window manager) dostarczanego wraz z XView. Ta wersja olvwm bazuje na
wersji 3 XView.

OpenLook był stylem używanym na starszych stacjach Suna, zanim Sun
wycofał się z niego i zaczął używać CDE. Nawet, gdy pojawiły się nowe,
niektórzy -- zwłaszcza uniksowi weterani -- chętnie pozostają przy olvwm
przypominającym im stare, dobre czasy, kiedy byli młodymi hackerami...

%prep
%setup -q -n %{name}.%{version} -a 1
%patch0 -p1

%build
xmkmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_wmpropsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

install olvwm $RPM_BUILD_ROOT%{_bindir}
install olwm.man $RPM_BUILD_ROOT%{_mandir}/man1/olwm.1
install olvwm.man $RPM_BUILD_ROOT%{_mandir}/man1/olvwm.1
install olvwmrc.man $RPM_BUILD_ROOT%{_mandir}/man5/olvwmrc.5

install %{SOURCE2} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LEGAL_NOTICE NEW_CHANGES CHANGES olvwm.info
%doc %dir config.examples
%attr(755,root,root) %{_bindir}/olvwm
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/%{name}.desktop
%{_mandir}/man[15]/*
