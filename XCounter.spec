Summary:	XCounter is simple traffic monitoring program.
Summary(pl):	XCounter jest prostym analizatorem ruchu w sieci.
Name:		XCounter
Version:	1.0.6
Release:	1
License:	GPLv2
Group:		Networking
Source0:	http://freshmeat.net/redir/xcounter/11865/url_tgz/%{name}-%{version}.tar.gz
URL:		http://freshmeat.net/redir/xcounter/11865/url_homepage/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Patch0:		%{name}-make.patch

%description
XCounter is simple monitoring program for Linux that displays
information about IP traffic on a selected interface.

%description -l pl
XCounter jest prostym analizatorem ruchu w sieci dla Linuksa.Pokazuje
obci±¿enie na wybranym interfejsie.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
        BINDIR=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf INSTALL ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
