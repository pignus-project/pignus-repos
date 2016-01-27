Summary:        Pignus package repositories
Name:           pignus-repos
Version:        25
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
Obsoletes:      pignus-repos-rawhide <= 25-0.3
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
* Wed Nov 16 2016 Lubomir Rintel <lkundrak@v3.sk> - 25-1
- Update fedora-repos for Pignus

* Wed Nov 02 2016 Mohan Boddu <mboddu@redhat.com> - 25-1
- setup for f25 final		
- disable updates-testing		
- set metadata expiry for fedora repo

* Mon Aug 08 2016 Dennis Gilmore <dennis@ausil.us> - 25-0.5
- fix up archmap file
- add f26 gpg keys

* Fri Jul 22 2016 Mohan Boddu <mboddu@redhat.com> - 25-0.4
- Disable Rawhide
- Enable fedora, updates, updates-testing

* Fri Jun 06 2016 Dennis Gilmore <dennis@ausil.us> - 25-0.3
- add the fedora build cisco shipped openh264 repo

* Thu Mar 31 2016 Dennis Gilmore <dennis@ausil.us> - 25-0.2
- add the Fedora 25 gpg keys

* Tue Feb 23 2016 Dennis Gilmore <dennis@ausil.us> - 25-0.1
- Setup for rawhide being f25
