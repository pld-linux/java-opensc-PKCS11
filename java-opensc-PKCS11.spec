%include	/usr/lib/rpm/macros.java
Summary:	PKCS#11 provider of the opensc project
Summary(pl.UTF-8):	Biblioteka z projektu opensc udostępniająca interfejs PKCS#11
Name:		java-opensc-PKCS11
Version:	0.2.2
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries/Java
#Source0Download: https://github.com/OpenSC/OpenSC-Java/releases
Source0:	https://github.com/OpenSC/OpenSC-Java/archive/pkcs11-%{version}.tar.gz
# Source0-md5:	075df87f1d4b10e765f71c9807be308f
URL:		https://github.com/OpenSC/OpenSC-Java
BuildRequires:	java-commons-logging >= 1.1
BuildRequires:	java-junit >= 3.8.1
BuildRequires:	java-log4j >= 1.2.13
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	libltdl-devel
BuildRequires:	maven
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
# for %{_javadir}
Requires:	jpackage-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PKCS#11 provider of the opensc project.

%description -l pl.UTF-8
Biblioteka z projektu opensc udostępniająca interfejs PKCS#11.

%prep
%setup -q -n OpenSC-Java-pkcs11-%{version}

%build
# FIXME: update build to use maven
export JAVA_HOME="%{java_home}"

required_jars="commons-logging log4j junit"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

#ant signedjarfile jnidist
mvn package # FIXME?

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir}}

# jars
cp -a dist/tmp/opensc-PKCS11.jar $RPM_BUILD_ROOT%{_javadir}/opensc-PKCS11-%{version}.jar
ln -s opensc-PKCS11-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/opensc-PKCS11.jar
install dist/tmp/libopensc-PKCS11-0.1.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/libopensc-PKCS11-0.1.so
%{_javadir}/opensc-PKCS11*.jar
