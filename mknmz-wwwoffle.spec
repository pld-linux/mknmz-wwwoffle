%include	/usr/lib/rpm/macros.perl
Summary:	Performs full-text search over the cache created by WWWOFFLE
Summary(pl):	Pe³notekstowe przeszukiwanie cache utworzonego przez WWWOFFLE
Name:		mknmz-wwwoffle
Version:	0.7.2
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://www.naney.org/comp/distrib/mknmz-wwwoffle/archive/%{name}-%{version}.tar.gz
# Source0-md5:	9258fa92d31d4894e898e61805d48d04
URL:		http://www.naney.org/comp/distrib/mknmz-wwwoffle/index.html
BuildRequires:	autoconf
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
