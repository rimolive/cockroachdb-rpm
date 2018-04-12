Name:       cockroach
Version:    v2.0.0
Release:    1%{?dist}
Summary:    CockroachDB - the open source, cloud-native SQL database
License:    Apache Public License 2.0
URL:        https://www.cockroachlabs.com/
Source0:    https://binaries.cockroachdb.com/%{name}-%{version}.src.tgz


BuildRequires: gcc
BuildRequires: golang
BuildRequires: cmake
BuildRequires: autoconf
BuildRequires: ncurses-devel

%description
CockroachDB is a distributed SQL database built on a transactional and strongly-consistent 
key-value store. It scales horizontally; survives disk, machine, rack, and even datacenter 
failures with minimal latency disruption and no manual intervention; supports 
strongly-consistent ACID transactions; and provides a familiar SQL API for structuring, 
manipulating, and querying data.

%prep
%setup -q

%build
%configure
%make %{_smp_mflags}

%install


%check
%make check


%files


%changelog
* Thu Apr 12 Ricardo Martinelli de Oliveira <rmartine@redhat.com>
- First package version