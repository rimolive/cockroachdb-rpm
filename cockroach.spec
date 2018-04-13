%define debug_package %{nil}

Name:       cockroach
Version:    2.0.0
Release:    1%{?dist}
Summary:    CockroachDB - the open source, cloud-native SQL database
License:    Apache Public License 2.0
URL:        https://www.cockroachlabs.com/
Source0:    https://binaries.cockroachdb.com/%{name}-v%{version}.src.tgz


BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: golang
BuildRequires: cmake
BuildRequires: autoconf
BuildRequires: ncurses-devel
# need to remove bundled version
BuildRequires: rocksdb-devel
BuildRequires: zlib-devel


%description
CockroachDB is a distributed SQL database built on a transactional and strongly-consistent 
key-value store. It scales horizontally; survives disk, machine, rack, and even datacenter 
failures with minimal latency disruption and no manual intervention; supports 
strongly-consistent ACID transactions; and provides a familiar SQL API for structuring, 
manipulating, and querying data.

%prep
%setup -q -n %{name}-v%{version}

%build
make buildoss

%install
install -Dpm 0755 src/github.com/cockroachdb/cockroach/cockroach %{buildroot}%{_bindir}/cockroach


%files
%{_bindir}/cockroach
%license  src/github.com/cockroachdb/cockroach/LICENSE
%doc src/github.com/cockroachdb/cockroach/README.md

%changelog
* Thu Apr 12 2018 Ricardo Martinelli de Oliveira <rmartine@redhat.com> - 2.0.0-1
- First package version
