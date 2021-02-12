%global __os_install_post %{nil}
%define artifactorylibdir /opt/jfrog/artifactory/var/bootstrap/artifactory/tomcat/lib

Name:           artifactory-sqljdbc-jar
Version:        0.0.1
Release:        0%{?dist}
Summary:        Supplimentary tools for JFrog Artifactory microservices
License:        GPLv3

Requires:       jfrog-artifactory-pro

BuildArch:      noarch

Source0:        mssql-jdbc-8.4.1.jre11.jar

%{?systemd_requires}

%description
Supplimentary tools for JFrog Artifactory microservices
Sets up following:
1. MSSQL JAR for Artifactory: Essential for MSSQL <-> Artifactory connections.

%prep

%build

%pre

%install
mkdir -p $RPM_BUILD_ROOT%{artifactorylibdir}
install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{artifactorylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%postun

%files
%attr(644,artifactory,artifactory) %{artifactorylibdir}

%changelog
* Fri Jan 29 2021 Varad Ghodake <varadghodake@gmail.com> 0.0.1-0 
- Initial RPM build
