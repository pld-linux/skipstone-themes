Summary:	SkipStone themes
Summary(pl):	Tematy do SkipStone
Name:		skipstone-themes
Version:	0.7.9
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://muhri.net/skipstone/images/themes/GoldStone.tar.gz
Source1:	http://muhri.net/skipstone/images/themes/SilverStone.tar.gz
Source2:	http://muhri.net/skipstone/images/themes/antarctic.skipstone.tar.gz
Source3:	http://muhri.net/skipstone/images/themes/aqua_blue.tar.gz
Source4:	http://muhri.net/skipstone/images/themes/aqua_white.tar.gz
Source5:	http://muhri.net/skipstone/images/themes/chrome.tar.gz
Source6:	http://muhri.net/skipstone/images/themes/gnome.tar.gz
Source7:	http://muhri.net/skipstone/images/themes/gold.tar.gz
Source8:	http://muhri.net/skipstone/images/themes/konquerer.tar.gz
Source9:	http://muhri.net/skipstone/images/themes/microgui.skipstone.tar.gz
Source10:	http://muhri.net/skipstone/images/themes/mozilla.tar.gz
Source11:	http://muhri.net/skipstone/images/themes/pixels.tar.gz
Source12:	http://muhri.net/skipstone/images/themes/revamped.skipstone.tar.gz
URL:		http://www.muhri.net/skipstone/images/themes/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libstdc++-devel
Requires:	skipstone = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir		/usr/X11R6/share/skipstone/pixmaps

%description
SkipStone Themes
engine.

%description -l pl
Tematy do SkipStone

%prep 
%setup -c -n %{name}-%{version}
%setup -T -c -D -a 1
%setup -T -c -D -a 2 
%setup -T -c -D -a 3
%setup -T -c -D -a 4
%setup -T -c -D -a 5
%setup -T -c -D -a 6
%setup -T -c -D -a 7
%setup -T -c -D -a 8
%setup -T -c -D -a 9
%setup -T -c -D -a 10
%setup -T -c -D -a 11
%setup -T -c -D -a 12 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}/{GoldStone,SilverStone,antarctic,aqua_blue,aqua_white,chrome,gnome,gold,Konquerer,microgui,mozilla,pixels,revamped}
for i in GoldStone SilverStone antarctic aqua_blue aqua_white chrome gnome gold Konquerer microgui mozilla pixels revamped; do
install ${i}/* $RPM_BUILD_ROOT%{_themesdir}/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022

%files
%defattr(644,root,root,755)
%{_themesdir}/GoldStone/*
%{_themesdir}/SilverStone/*
%{_themesdir}/antarctic/*
%{_themesdir}/aqua_blue/*
%{_themesdir}/aqua_white/*
%{_themesdir}/chrome/*
%{_themesdir}/gnome/*
%{_themesdir}/gold/*
%{_themesdir}/Konquerer/*
%{_themesdir}/microgui/*
%{_themesdir}/mozilla/*
%{_themesdir}/pixels/*
%{_themesdir}/revamped/*
