Summary:	XCounter - simple traffic monitoring program
Summary(pl):	XCounter - prosty analizator ruchu w sieci
Name:		XCounter
Version:	1.0.6
Release:	2
License:	GPL v2
Group:		Applications/Networking
#Source0Download: http://members.fortunecity.com/mrsi/xcounter.html
Source0:	http://isp.od.ua/~rsi/%{name}-%{version}.tar.gz
# Source0-md5:	ad50093d6e588335bee5660716abc92f
Patch0:		%{name}-make.patch
URL:		http://members.fortunecity.com/mrsi/xcounter.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCounter is simple monitoring program for Linux that displays
information about IP traffic on a selected interface.

%description -l pl
XCounter jest prostym analizatorem ruchu w sieci dla Linuksa. Pokazuje
obci±¿enie na wybranym interfejsie.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	FLAGS="%{rpmcflags}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        BINDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%lang(ru) %doc README.RU
%attr(755,root,root) %{_bindir}/*
