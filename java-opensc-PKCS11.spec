%include	/usr/lib/rpm/macros.java
Summary:	PKCS#11 provider of the opensc project
Summary(pl.UTF-8):	Biblioteka z projektu opensc udostępniająca interfejs PKCS#11
Name:		java-opensc-PKCS11
Version:	0.1.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Java
Source0:	http://www.opensc-project.org/files/opensc-java/opensc-PKCS11-src-%{version}.zip
# Source0-md5:	b58ebd345e915110b79c6a68d21c2fc3
URL:		http://www.opensc-project.org/
BuildRequires:	ant
BuildRequires:	java-commons-logging
# >= 1.1
BuildRequires:	java-log4j >= 1.2.13
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 4.1
BuildRequires:	libltdl-devel
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
%setup -q -c

%build
export JAVA_HOME="%{java_home}"

required_jars="commons-logging log4j junit"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH

%ant signedjarfile jnidist

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
%doc README
%attr(755,root,root) %{_libdir}/libopensc-PKCS11-0.1.so
%{_javadir}/opensc-PKCS11*.jar
