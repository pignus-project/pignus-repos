Summary:        Pignus package repositories
Name:           pignus-repos
Version:        23
Release:        1
License:        MIT
Group:          System Environment/Base
URL:            https://pignus.computer/

Source1:        pignus-rawhide.repo
Source2:        pignus.repo
Source3:        pignus-updates.repo
Source4:        pignus-updates-testing.repo

Provides:       pignus-repos(%{version})
Requires:       system-release(%{version})
Obsoletes:      pignus-repos-rawhide <= 23-0.2
Obsoletes:      pignus-repos-anaconda < 22-0.3
BuildArch:      noarch

%description
Pignus package repository files for yum and dnf along with gpg public keys

%package rawhide
Summary:        Rawhide repo definitions
Requires:       pignus-repos = %{version}-%{release}
Obsoletes:      pignus-release-rawhide <= 22-0.3

%description rawhide
This package provides the rawhide repo definitions.


%prep

%build

%install
# Install the keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
#install -m 644 RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done


%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/pignus.repo
%config(noreplace) /etc/yum.repos.d/pignus-updates*.repo
%dir /etc/pki/rpm-gpg
#/etc/pki/rpm-gpg/*

%files rawhide
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/pignus-rawhide.repo

%changelog
* Wed Jan 27 2016 Lubomir Rintel <lkundrak@v3.sk> - 23-2
- Update for Pignus Alpha

* Mon Oct 19 2015 Dennis Gilmore <dennis@ausil.us> - 23-1
- setup for Fedora 23 GA
- disable updates-testing
- set fedora repodata expiry at 28 days
- add all Fedora gpg keys

* Tue Jul 14 2015 Dennis Gilmore <dennis@ausil.us> - 23-0.4
- disable rawhide
- enable fedora, updates, updates-testing

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Dennis Gilmore <dennis@ausil.us> - 23-0.2
- add the Fedora 23 gpg keys

* Tue Feb 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 23-0.1
- Setup for f23 rawhide
