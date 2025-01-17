Name:           drupal
Version:        7.14
Release:        3
Source0:        http://ftp.osuosl.org/pub/drupal/files/projects/%{name}-%{version}.tar.gz
Patch0:		drupal-7.2-baseurl.patch
Summary:        Open source content management platform
URL:            https://www.drupal.org/
License:        GPLv2+
Group:          Networking/WWW
Requires:       apache
Requires:       apache-mod_php
Requires:       php-xml
Requires:       php-mbstring
Requires:	php-gd
Suggests:	drupal-database-storage
BuildArch:      noarch

%description
Drupal is a free software package that allows an individual or a 
community of users to easily publish, manage and organize a wide variety 
of content on a website. Tens of thousands of people and organizations 
have used Drupal to power scores of different web sites, including

    * Community web portals
    * Discussion sites
    * Corporate web sites
    * Intranet applications
    * Personal web sites or blogs
    * Aficionado sites
    * E-commerce applications
    * Resource directories
    * Social Networking sites

%package mysql
Summary: mysql storage of drupal
Group: Networking/WWW
Provides: drupal-database-storage = %{EVRD}
Requires: drupal = %{version}
Requires: php-pdo_mysql
Requires: mysql
Obsoletes: drupal-mysqli < %{version}

%description mysql
This package provides virtual requries of using mysql as storage backend
for drupal.

%package postgresql
Summary: postgresql storage of drupal
Group: Networking/WWW
Provides: drupal-database-storage = %{EVRD}
Requires: drupal = %{version}
Requires: php-pdo_pgsql
Requires: postgresql-virtual

%description postgresql
This package provides virtual requries of using postgresql as storage backend
for drupal.

%package sqlite
Summary: sqlite storage of drupal
Group: Networking/WWW
Provides: drupal-database-storage = %{EVRD}
Requires: drupal = %{version}
Requires: php-pdo_sqlite

%description sqlite
This package provides virtual requries of using sqlite as storage backend
for drupal.

%prep
%setup -q 
%patch0 -p0

%install
%{__mkdir_p} %{buildroot}%{_var}/www/drupal
cp -a * %{buildroot}%{_var}/www/drupal

%{__rm} %{buildroot}%{_var}/www/drupal/*.txt %{buildroot}%{_var}/www/drupal/web.config

%{__mkdir_p} %{buildroot}%{_sysconfdir}/drupal
%{__cat} > %{buildroot}%{_sysconfdir}/drupal/robots.txt << EOF
User-agent: *
Disallow:   /
EOF
(cd %{buildroot}%{_var}/www/drupal && \
%{__ln_s} %{_sysconfdir}/drupal/robots.txt robots.txt)

%{__mkdir_p} %{buildroot}%{_webappconfdir}
cp .htaccess %{buildroot}%{_webappconfdir}/drupal.conf

%files
%defattr(0644,root,root,0755)
%doc *.txt
%dir %{_var}/www/drupal
%{_var}/www/drupal/*.php
%{_var}/www/drupal/*.txt
%{_var}/www/drupal/includes
%{_var}/www/drupal/misc
%{_var}/www/drupal/modules
%{_var}/www/drupal/profiles
%dir %{_var}/www/drupal/scripts
%attr(0755,root,root) %{_var}/www/drupal/scripts/*
%attr(0755,apache,apache) %{_var}/www/drupal/sites
%{_var}/www/drupal/themes
%attr(710,root,apache) %dir %{_sysconfdir}/drupal
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/drupal/robots.txt
%config(noreplace) %{_webappconfdir}/drupal.conf

%files mysql

%files postgresql

%files sqlite
