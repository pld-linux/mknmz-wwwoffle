# XXX is this right - it was /var/lib before FHS macros
%define _localstatedir	/var/cache/wwwoffle/search/namazu

Summary:	Performs full-text search over the cache created by WWWOFFLE
Name:		mknmz-wwwoffle
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Text
#BuildRequires:	perl >= 5.6.0, perl-NKF >= 1.70, perl-Text-Kakasi >= 1.00
#Requires:	perl >= 5.6.0, perl-File-MMagic >= 1.12, perl-NKF >= 1.70
#Requires:	kakasi >= 2.3.0, perl-Text-Kakasi >= 1.00
Source0:	http://www.naney.org/comp/distrib/mknmz-wwwoffle/archive/%{name}-%{version}.tar.gz
URL:		http://www.naney.org/comp/distrib/mknmz-wwwoffle/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mknmz-wwwoffle performs full-text search over the cache created by
WWWOFFLE, using full-text search system Namazu
(http://www.namazu.org/). It adds a filter for mknmz which is used to
generate index files for cache entries in WWWOFFLE.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%doc README README.ja NEWS THANKS INSTALL ChangeLog AUTHORS
%dir %{_localstatedir}
%attr(755,root,root) %{_bindir}/mknmz-wwwoffle
%{_mandir}/man1/*
%{_datadir}/namazu/filter/*
