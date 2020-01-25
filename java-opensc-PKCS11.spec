# TODO: fix build without network
Summary:	PKCS#11 provider of the OpenSC project
Summary(pl.UTF-8):	Biblioteka z projektu OpenSC udostępniająca interfejs PKCS#11
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
PKCS#11 provider of the OpenSC project.

%description -l pl.UTF-8
Biblioteka z projektu OpenSC udostępniająca interfejs PKCS#11.

%prep
%setup -q -n OpenSC-Java-pkcs11-%{version}

cat >> jni/build/unix/release/config.data <<EOF
ac CC=%{__cc}
ac CFLAGS=%{rpmcflags} -fno-stack-protector -Wall
ac CPPFLAGS=%{rpmcppflags}
ac LDFLAGS=%{rpmldflags}
EOF

%build
# FIXME: update build to use maven
export JAVA_HOME="%{java_home}"

# TODO: how to disable downloading in maven?
#required_jars="commons-logging log4j junit"
#CLASSPATH=$(build-classpath $required_jars)
#export CLASSPATH

# FIXME: any options required?
mvn package

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir}}

# jar
cp -p target/opensc-PKCS11-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s opensc-PKCS11-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/opensc-PKCS11.jar
# jni
install target/lib/libopensc-PKCS11-0.2.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/libopensc-PKCS11-0.2.so
%{_javadir}/opensc-PKCS11*.jar
