%define rbname usb
%define version 0.2
%define release %mkrel 2

Summary:	Ruby binding for libusb
Name:		ruby-%{rbname}
Version:	%{version}
Release:	%{release}
Group:		Development/Ruby
License:	GPL
URL:		http://www.a-k-r.org/ruby-usb/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	ruby-devel
BuildRequires:	libusb-devel

%description
libusb binding library for Ruby

%prep
%setup -q

%build
ruby extconf.rb --vendor
make

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING ChangeLog 
%{ruby_vendorlibdir}/*
%{ruby_vendorarchdir}/*


