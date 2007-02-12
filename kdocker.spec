Summary:	System tray docker for applications
Summary(pl.UTF-8):   Program do dokowania aplikacji w zasobniku systemowym
Name:		kdocker
Version:	1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kdocker/%{name}-%{version}.tar.gz
# Source0-md5:	c6900fc87c6c48cd106457ed9c6f924f
Source1:	%{name}.desktop
URL:		http://kdocker.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDocker docks any application in the system tray. This makes it
possible to dock OpenOffice, XMMS, Firefox, Thunderbird, and other
programs. Works for KDE, GNOME, Xfce and many more.

%description -l pl.UTF-8
KDocker pozwala na dokowanie każdej aplikacji w zasobniku systemowym.
Pozwala to na dokowanie OpenOffice'a, XMMS-a, Firefoksa, Thunderbirda
i innych programów. Jest zgodny z KDE, GNOME, Xfce i wieloma innymi.

%prep
%setup -q -n %{name}

%build
sed -i -e 's/\/local//' kdocker.pro
qmake
sed -i -e 's/-lqt/-lqt-mt/' Makefile
sed -i -e 's/lib/%{_lib}/' Makefile
%{__make} \
	QTDIR='%{_prefix}'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	QTDIR='%{_prefix}'

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
