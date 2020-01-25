Summary:	Performs full-text search over the cache created by WWWOFFLE
Summary(pl.UTF-8):	Pełnotekstowe przeszukiwanie cache utworzonego przez WWWOFFLE
Name:		mknmz-wwwoffle
Version:	0.7.2
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://www.naney.org/comp/distrib/mknmz-wwwoffle/archive/%{name}-%{version}.tar.gz
# Source0-md5:	9258fa92d31d4894e898e61805d48d04
URL:		http://www.naney.org/comp/distrib/mknmz-wwwoffle/index.html
BuildRequires:	autoconf
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-DB_File
Requires:	namazu
Requires:	perl-DB_File
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nknmz-wwwoffle performs full-text search over the cache created by
wwwoffle, using full-text search system Namazu
(http://www.namazu.org/). It adds a filter for mknmz which is used to
generate index files for cache entries in wwwoffle.

%description -l pl.UTF-8
mknmz-wwwoffle przeprowadza pełnotekstowe przeszukiwanie cache
utworzonego przez wwwoffle, używając systemu przeszukiwania
pełnotekstowego Namazu (http://www.namazu.org/). mknmz-wwwoffle dodaje
filtr dla mknmz, który jest używany do generowania plików indeksowych
dla cache z wwwoffle.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%lang(ja) %doc README.ja
%attr(755,root,root) %{_bindir}/mknmz-wwwoffle
%{_mandir}/man1/*
%{_datadir}/namazu/filter/*
