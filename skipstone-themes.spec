Summary:	SkipStone themes
Summary(pl.UTF-8):	Motywy do SkipStone
Name:		skipstone-themes
Version:	0.7.9
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://muhri.net/skipstone/images/themes/GoldStone.tar.gz
# Source0-md5:	07ef5124e7a2ab9e0a4ae612c77cc1c8
Source1:	http://muhri.net/skipstone/images/themes/SilverStone.tar.gz
# Source1-md5:	d4623c4673a82a5fa6d4aef7e13602cc
Source2:	http://muhri.net/skipstone/images/themes/antarctic.skipstone.tar.gz
# Source2-md5:	6cb38238161001b95026ba7521e154dd
Source3:	http://muhri.net/skipstone/images/themes/aqua_blue.tar.gz
# Source3-md5:	6c33535b1d2220f810214396b40d9999
Source4:	http://muhri.net/skipstone/images/themes/aqua_white.tar.gz
# Source4-md5:	96998e4034bf0917ac208bc185c45db8
Source5:	http://muhri.net/skipstone/images/themes/chrome.tar.gz
# Source5-md5:	250ea8215bcfe4349de3c56e671fe2cf
Source6:	http://muhri.net/skipstone/images/themes/gnome.tar.gz
# Source6-md5:	029dee0cec4b759b69c5e04645f3d770
Source7:	http://muhri.net/skipstone/images/themes/gold.tar.gz
# Source7-md5:	7dc0056843bdf1856fa9b7c7eadcff9c
Source8:	http://muhri.net/skipstone/images/themes/konquerer.tar.gz
# Source8-md5:	13847f46ffbd3b7da6844e057ad8111b
Source9:	http://muhri.net/skipstone/images/themes/microgui.skipstone.tar.gz
# Source9-md5:	d676b354ecff5479702bb98df60a43a7
Source10:	http://muhri.net/skipstone/images/themes/mozilla.tar.gz
# Source10-md5:	8ba7d7c704079ec72cfefe48c412d44d
Source11:	http://muhri.net/skipstone/images/themes/pixels.tar.gz
# Source11-md5:	16ceb42ca7f1518f77c9901fce8ad9ab
Source12:	http://muhri.net/skipstone/images/themes/revamped.skipstone.tar.gz
# Source12-md5:	7063a16eb74fad1dc62788f8d06db347
URL:		http://www.muhri.net/skipstone/images/themes/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libstdc++-devel
Requires:	skipstone => %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/skipstone/pixmaps

%description
SkipStone Themes engine.

%description -l pl.UTF-8
Motywy do SkipStone.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12

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
