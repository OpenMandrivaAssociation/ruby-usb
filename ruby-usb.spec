%define rbname usb
%define version 0.1
%define release %mkrel 1

Summary:	Ruby binding for libusb
Name:		ruby-%{rbname}
Version:	%{version}
Release:	%{release}
Group:		Development/Ruby
License:	GPL
URL:		http://www.a-k-r.org/ruby-usb/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ruby-usb-0.1-st_table.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	ruby-devel
BuildRequires:	libusb-devel

%description
libusb binding library for Ruby

%prep
%setup -q
%patch0 -p0 

%build
ruby extconf.rb
make

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog 
%{ruby_sitelibdir}/*
%{ruby_sitearchdir}/*


