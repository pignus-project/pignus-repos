Summary:        Pignus package repositories
Name:           pignus-repos
Version:        26
Release:        0.8.pi1
License:        MIT
Group:          System Environment/Base
URL:            https://pignus.computer/

Source1:        pignus-rawhide.repo
Source2:        pignus.repo
Source3:        pignus-updates.repo
Source4:        pignus-updates-testing.repo

Provides:       pignus-repos(%{version})
Requires:       system-release(%{version})
Obsoletes:      pignus-repos-rawhide <= 26-0.3
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
* Sat Apr 08 2017 Lubomir Rintel <lkundrak@v3.sk> - 26-0.8
- Update fedora-repos for Pignus

* Mon Mar 02 2017 Mohan Boddu <mboddu@redhat.com> - 26-0.8
- Fix up obsoletes fedora-repos-rawhide versioning

* Mon Feb 27 2017 Mohan Boddu <mboddu@redhat.com> - 26-0.7
- Fix up dependencies

* Mon Feb 27 2017 Mohan Boddu <mboddu@redhat.com> - 26-0.6
- Disable Rawhide
- Enable fedora, updates, updates-testing

* Thu Feb 23 2017 Dennis Gilmore <dennis@ausil.us> - 26-0.5
- add the Fedora 27 key and matching archmap entry

* Mon Sep 26 2016 Dennis Gilmore <dennis@ausil.us> - 26-0.4
- enable gpgcheck on rawhide

* Wed Sep 14 2016 Dennis Gilmore <dennis@ausil.us> - 26-0.3
- fix up baseurl lines
- replace f26 gpg key for wrong uid
- add zypper support rhbz#1373317
- sign aarch64 with primary key

* Mon Aug 08 2016 Dennis Gilmore <dennis@ausil.us> - 26-0.2
- fix up archmap file
- add f26 gpg keys

* Fri Jul 22 2016 Mohan Boddu <mboddu@redhat.com> - 26-0.1
- Setup for rawhide being f26
