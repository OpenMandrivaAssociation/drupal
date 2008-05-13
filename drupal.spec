Name:           drupal
Version:        6.2
Release:        %mkrel 2
Epoch:          0
Source0:        http://ftp.osuosl.org/pub/drupal/files/projects/%name-%version.tar.gz
Source1:        http://ftp.drupal.org/files/projects/biblio-6.x-1.0-beta3.tar.gz
Patch0:		drupal-6.2-baseurl.patch
Summary:        Open source content management platform
URL:            http://www.drupal.org/
License:        GPLv2+
Group:          Networking/WWW
Requires:       apache
Requires:       apache-mod_php
Requires:       php-xml
Requires:       php-mbstring
Requires(post): rpm-helper
Requires(postun): rpm-helper
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep
%setup -q 
%patch0 -p0

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_var}/www/drupal
%{__cp} -a * %{buildroot}%{_var}/www/drupal
%{__tar} xf %{SOURCE1} -C %{buildroot}%{_var}/www/drupal/modules

%{__rm} %{buildroot}%{_var}/www/drupal/*.txt

%{__mkdir_p} %{buildroot}%{_sysconfdir}/drupal
%{__cat} > %{buildroot}%{_sysconfdir}/drupal/robots.txt << EOF
User-agent: *
Disallow:   /
EOF
(cd %{buildroot}%{_var}/www/drupal && \
%{__ln_s} %{_sysconfdir}/drupal/robots.txt robots.txt)

%{__mkdir_p} %{buildroot}%{_webappconfdir}
%{__cat} > %{buildroot}%{_webappconfdir}/drupal.conf << EOF
Alias /drupal %{_var}/www/drupal

<Directory %{_var}/www/drupal>
    Options +FollowSymLinks
    AllowOverride All
    Order allow,deny
    Allow from all
</Directory>
EOF

%clean
%{__rm} -rf %{buildroot}

%post
%{_post_webapp}

%postun
%{_postun_webapp}

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
%{_var}/www/drupal/sites
%{_var}/www/drupal/themes
%attr(710,root,apache) %dir %{_sysconfdir}/drupal
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/drupal/robots.txt
%config(noreplace) %{_webappconfdir}/drupal.conf
