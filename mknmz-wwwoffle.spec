Summary:	Performs full-text search over the cache created by WWWOFFLE
Summary(pl):	Przeprowadza pe³notekstowe przeszukiwanie cache utworzonego przez WWWOFFLE
Name:		mknmz-wwwoffle
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Text
BuildRequires:	autoconf
#BuildRequires:	perl >= 5.6.0, perl-NKF >= 1.70, perl-Text-Kakasi >= 1.00
#Requires:	perl >= 5.6.0, perl-File-MMagic >= 1.12, perl-NKF >= 1.70
#Requires:	kakasi >= 2.3.0, perl-Text-Kakasi >= 1.00
Source0:	http://www.naney.org/comp/distrib/mknmz-wwwoffle/archive/%{name}-%{version}.tar.gz
# Source0-md5:	9258fa92d31d4894e898e61805d48d04
URL:		http://www.naney.org/comp/distrib/mknmz-wwwoffle/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# XXX is this right - it was /var/lib before FHS macros
%define _localstatedir	/var/cache/wwwoffle/search/namazu

%description
nknmz-wwwoffle performs full-text search over the cache created by
wwwoffle, using full-text search system Namazu
(http://www.namazu.org/). It adds a filter for mknmz which is used to
generate index files for cache entries in wwwoffle.

%description -l pl
mknmz-wwwoffle przeprowadza pe³notekstowe przeszukiwanie cache
utworzonego przez wwwoffle, u¿ywaj±c systemu przeszukiwania
pe³notekstowego Namazu (http://www.namazu.org/). mknmz-wwwoffle dodaje
filtr dla mknmz, który jest u¿ywany do generowania plików indeksowych
dla cache z wwwoffle.

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS THANKS INSTALL ChangeLog AUTHORS
%lang(ja) %doc README.ja
%dir %{_localstatedir}
%attr(755,root,root) %{_bindir}/mknmz-wwwoffle
%{_mandir}/man1/*
%{_datadir}/namazu/filter/*
