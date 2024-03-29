# TODO
# - inetd service for other end
%define		plugin	check_nagios_summary
Summary:	Distributed Nagios monitoring enabler
Name:		nagios-plugin-%{plugin}
Version:	0.0.27
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.vanheusden.com/check_nagios_summary/%{plugin}-%{version}.tgz
# Source0-md5:	0557ae26b11b884b762b54f340559838
Source1:	%{plugin}.cfg
Patch0:		%{name}.patch
URL:		http://www.vanheusden.com/check_nagios_summary/
BuildRequires:	libstdc++-devel
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%description
check_nagios_summary enables you to do perform distributed monitoring
using Nagios. With this plugin, a Nagios system can check and
summarize the status of other (satelite) Nagios systems.

%prep
%setup -q -n %{plugin}-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	DEBUG="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install %{plugin} $RPM_BUILD_ROOT%{_plugindir}
%{__sed} -e 's,@plugindir@,%{_plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{_plugindir}/%{plugin}
