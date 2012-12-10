Name:           drupal
Version:        7.14
Release:        1
Source0:        http://ftp.osuosl.org/pub/drupal/files/projects/%name-%version.tar.gz
Patch0:		drupal-7.2-baseurl.patch
Summary:        Open source content management platform
URL:            http://www.drupal.org/
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
Summary: mysql storage of druapl
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
Summary: sqlite storage of druapl
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


%changelog
* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.14-1
+ Revision: 798225
- update to 7.14

* Sun Feb 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0:7.12-1
+ Revision: 771308
- version update 7.12

* Tue Oct 11 2011 Funda Wang <fwang@mandriva.org> 0:7.8-1
+ Revision: 704244
- new version 7.8

* Thu Jul 07 2011 Funda Wang <fwang@mandriva.org> 0:7.4-1
+ Revision: 689048
- update to new version 7.4

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0:7.2-1
+ Revision: 681642
- new version 7.2

* Sat Jan 08 2011 Funda Wang <fwang@mandriva.org> 0:7.0-1mdv2011.0
+ Revision: 630576
- new version 7.0

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 0:6.20-1mdv2011.0
+ Revision: 622382
- update to new version 6.20

* Sun Aug 15 2010 Funda Wang <fwang@mandriva.org> 0:6.19-1mdv2011.0
+ Revision: 570187
- update to new version 6.19

* Tue Jul 27 2010 Jerome Martin <jmartin@mandriva.org> 0:6.17-1mdv2011.0
+ Revision: 561158
- Release 6.17

* Fri Mar 05 2010 Funda Wang <fwang@mandriva.org> 0:6.16-1mdv2010.1
+ Revision: 514438
- New version 6.16

* Mon Mar 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0:6.15-2mdv2010.1
+ Revision: 513130
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Thu Dec 17 2009 Funda Wang <fwang@mandriva.org> 0:6.15-1mdv2010.1
+ Revision: 479651
- rediff baseurl patch
- new version 6.15

* Thu Sep 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0:6.14-1mdv2010.0
+ Revision: 444140
- update to new version 6.14

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 0:6.13-4mdv2010.0
+ Revision: 410916
- add dependency for main pacakge
- add several virtual provides to ease users

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 0:6.13-2mdv2010.0
+ Revision: 410890
- add php-gd for its dependency (bug#51786)
- fix perm of sites subdir (bug#52682)

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0:6.13-1mdv2010.0
+ Revision: 399044
- update to new version 6.13

* Thu May 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0:6.12-1mdv2010.0
+ Revision: 375765
- update to new version 6.12

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0:6.11-1mdv2010.0
+ Revision: 370003
- New version 6.11

* Sat Mar 14 2009 Funda Wang <fwang@mandriva.org> 0:6.10-1mdv2009.1
+ Revision: 354970
- New version 6.10

* Fri Jan 16 2009 Funda Wang <fwang@mandriva.org> 0:6.9-1mdv2009.1
+ Revision: 330090
- New version 6.9

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 0:6.8-1mdv2009.1
+ Revision: 314236
- new version 6.8

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 0:6.7-1mdv2009.1
+ Revision: 312863
- rediff baseurl patch
- new version 6.7

* Thu Oct 23 2008 Funda Wang <fwang@mandriva.org> 0:6.6-1mdv2009.1
+ Revision: 296651
- update to new version 6.6

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0:6.5-1mdv2009.1
+ Revision: 292746
- update to new version 6.5

* Thu Aug 14 2008 Funda Wang <fwang@mandriva.org> 0:6.4-1mdv2009.0
+ Revision: 271698
- New version 6.4

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 0:6.3-3mdv2009.0
+ Revision: 250565
- drop /var/www/drupal/.htaccess, put all the stuff into webapps.conf

* Fri Jul 25 2008 Funda Wang <fwang@mandriva.org> 0:6.3-2mdv2009.0
+ Revision: 248194
- add htaccess file

* Thu Jul 10 2008 Funda Wang <fwang@mandriva.org> 0:6.3-1mdv2009.0
+ Revision: 233274
- update to new version 6.3

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0:6.2-2mdv2009.0
+ Revision: 206530
- clearify default baseurl
- drupal now has a beautiful installer

* Sat Apr 12 2008 Funda Wang <fwang@mandriva.org> 0:6.2-1mdv2009.0
+ Revision: 192607
- New version 6.2

* Sun Mar 02 2008 Funda Wang <fwang@mandriva.org> 0:6.1-1mdv2008.1
+ Revision: 177600
- New version 6.1

* Sat Feb 16 2008 David Walluck <walluck@mandriva.org> 0:6.0-1mdv2008.1
+ Revision: 169228
- fix install
- fix mixed-use-of-spaces-and-tabs
- 6.0

* Tue Jan 29 2008 Funda Wang <fwang@mandriva.org> 0:5.7-1mdv2008.1
+ Revision: 159770
- New version 5.7

* Fri Jan 11 2008 Funda Wang <fwang@mandriva.org> 0:5.6-1mdv2008.1
+ Revision: 147909
- update to new version 5.6
- requires mbstring
- new license policy
- requires php-xml

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Funda Wang <fwang@mandriva.org> 0:5.5-1mdv2008.1
+ Revision: 116118
- update to new version 5.5

* Fri Oct 19 2007 Pascal Terjan <pterjan@mandriva.org> 0:5.3-1mdv2008.1
+ Revision: 100221
- update to new version 5.3

* Mon Aug 06 2007 Funda Wang <fwang@mandriva.org> 0:5.2-1mdv2008.0
+ Revision: 59415
- New version 5.2


* Thu Mar 08 2007 David Walluck <walluck@mandriva.org> 5.1-1mdv2007.1
+ Revision: 134958
- 5.1
- Import drupal

* Fri May 05 2006 Lenny Cartier <lenny@mandriva.com> 4.7.0-1mdk
- 4.7.0

* Sat May 08 2004 Robert Vojta <robert.vojta@mandrake.cz> 4.4.0-2mdk
- rebuild (bug #9709)

* Fri Apr 16 2004 Daouda LO <daouda@mandrakesoft.com> 4.4.0-1mdk
- first mandrake package

