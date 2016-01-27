Summary:        Pignus package repositories
Name:           pignus-repos
Version:        24
Release:        0.5
License:        MIT
Group:          System Environment/Base
URL:            https://pignus.computer/

Source1:        pignus-rawhide.repo
Source2:        pignus.repo
Source3:        pignus-updates.repo
Source4:        pignus-updates-testing.repo

Provides:       pignus-repos(%{version})
Requires:       system-release(%{version})
Obsoletes:      pignus-repos-rawhide <= 24-0.2
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
* Mon May 09 2016 Lubomir Rintel <lkundrak@v3.sk> - 24-0.5
- Update fedora-repos for Pignus

* Tue Feb 23 2016 Dennis Gilmore <dennis@ausil.us> - 24-0.4
- setup for f24 branching
- Obsolete older fedora-repos-rawhide
- disable rawhide
- enable fedora, updates and updates-testing

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 24-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Dennis Gilmore <dennis@ausil.us> - 24-0.2
- add all keys f7 up to f24 rhbz#1246701

* Tue Jul 14 2015 Dennis Gilmore <dennis@ausil.us> - 24-0.1
- Setup for rawhide being f24
