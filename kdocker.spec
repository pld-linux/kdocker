Summary:	System tray docker for applications
Summary(pl):	Program do dokowania aplikacji w zasobniku systemowym
Name:		kdocker
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kdocker/%{name}-%{version}.tar.gz
# Source0-md5:	b2c5b0aec0da8323159625d782eff409
# Source0-size:	446771
Source1:	%{name}.desktop
URL:		http://kdocker.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDocker docks any application in the system tray. This makes it
possible to dock openoffice, xmms, firefox, thunderbird, and other
programs. Works for KDE, GNOME, XFce and many more.

%description -l pl
KDocker pozwala na dokowanie ka¿dej aplikacji w zasobniku systemowym.
Pozwala to na dokowanie openoffice'a, xmmsa, firefoxa, thunderbirda i
innych programów. Jest zgodny z KDE, GNOME, XFce i wieloma innymi.

%prep
%setup -q -n %{name}

%build
%{__perl} -pi -e 's/\/local//' kdocker.pro
qmake
%{__perl} -pi -e 's/-lqt/-lqt-mt/' Makefile
%{__make} QTDIR='%{_prefix}'

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
%{_desktopdir}/*
