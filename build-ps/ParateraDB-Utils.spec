Name:       ParateraDB-Utils	
Version:    1.0.1
Release:	1%{?dist}
Summary:	ParateraDB Utils Tools.

Group:      Databases/ParateraDB	
License:    Copyright(c) 2015	
URL:	    https://git.paratera.net/dba/ParateraDB-Utils	
Source0:    https://git.paratera.net/dba/%{name}.tar.gz	


BuildRequires: coreutils grep procps shadow-utils gcc-c++ gperf ncurses-devel perl readline-devel time zlib-devel libaio-devel bison cmake make automake	
Requires: mailx tar openssl grep coreutils procps shadow-utils perl time pigz ParateraDB-Backup ParateraDB-Server-server-56 ParateraDB-Server-client-56 perl-IO-Socket-SSL perl-Net-LibIDN perl-Net-SSLeay perl-TermReadKey	

%description
    ParateraDB Utils Tools.

%prep
%setup -q -n %{name}


%build
make %{?_smp_mflags}


%install

RBR=$RPM_BUILD_ROOT
MBD=$RPM_BUILD_DIR/%{name}

install -D -m 0755 $MBD/read_metadata $RBR/%{_bindir}/read_metadata
install -D -m 0755 $MBD/registe_metadata $RBR/%{_bindir}/registe_metadata
install -D -m 0755 $MBD/support-scripts/DatabaseBackup.sh $RBR/%{_bindir}/DatabaseBackup
install -D -m 0755 $MBD/support-scripts/CompressDbxBak.sh $RBR/%{_bindir}/CompressDbxBak
install -D -m 0755 $MBD/support-scripts/NfsMount.sh $RBR/%{_bindir}/NfsMount
install -D -m 0755 $MBD/support-scripts/RemoveDbxBak.sh $RBR/%{_bindir}/RemoveDbxBak
install -D -m 0755 $MBD/support-scripts/SyncDBxBak.sh $RBR/%{_bindir}/SyncDBxBak
install -D -m 0755 $MBD/support-scripts/pt-align $RBR/%{_bindir}/pt-align
install -D -m 0755 $MBD/support-scripts/pt-archiver $RBR/%{_bindir}/pt-archiver
install -D -m 0755 $MBD/support-scripts/pt-config-diff $RBR/%{_bindir}/pt-config-diff
install -D -m 0755 $MBD/support-scripts/pt-deadlock-logger $RBR/%{_bindir}/pt-deadlock
install -D -m 0755 $MBD/support-scripts/pt-diskstats $RBR/%{_bindir}/pt-diskstats
install -D -m 0755 $MBD/support-scripts/pt-duplicate-key-checker $RBR/%{_bindir}/pt-duplicate-key-checker
install -D -m 0755 $MBD/support-scripts/pt-fifo-split $RBR/%{_bindir}/pt-fifo-split
install -D -m 0755 $MBD/support-scripts/pt-find $RBR/%{_bindir}/pt-find
install -D -m 0755 $MBD/support-scripts/pt-fingerprint $RBR/%{_bindir}/pt-fingerprint
install -D -m 0755 $MBD/support-scripts/pt-fk-error-logger $RBR/%{_bindir}/pt-fk-error-logger
install -D -m 0755 $MBD/support-scripts/pt-heartbeat $RBR/%{_bindir}/pt-heartbeatd
install -D -m 0755 $MBD/support-scripts/pt-index-usage $RBR/%{_bindir}/pt-index-usage
install -D -m 0755 $MBD/support-scripts/pt-ioprofile $RBR/%{_bindir}/pt-ioprofile
install -D -m 0755 $MBD/support-scripts/pt-kill $RBR/%{_bindir}/pt-kill
install -D -m 0755 $MBD/support-scripts/pt-mext $RBR/%{_bindir}/pt-mext
install -D -m 0755 $MBD/support-scripts/pt-mysql-summary $RBR/%{_bindir}/pt-mysql-summary
install -D -m 0755 $MBD/support-scripts/pt-online-schema-change $RBR/%{_bindir}/pt-online-schema-change
install -D -m 0755 $MBD/support-scripts/pt-pmp $RBR/%{_bindir}/pt-pmp
install -D -m 0755 $MBD/support-scripts/pt-query-digest $RBR/%{_bindir}/pt-query-digest
install -D -m 0755 $MBD/support-scripts/pt-show-grants $RBR/%{_bindir}/pt-show-grants
install -D -m 0755 $MBD/support-scripts/pt-sift $RBR/%{_bindir}/pt-sift
install -D -m 0755 $MBD/support-scripts/pt-slave-delay $RBR/%{_bindir}/pt-slave-delay
install -D -m 0755 $MBD/support-scripts/pt-slave-find $RBR/%{_bindir}/pt-slave-find
install -D -m 0755 $MBD/support-scripts/pt-slave-restart $RBR/%{_bindir}/pt-slave-restart
install -D -m 0755 $MBD/support-scripts/pt-stalk $RBR/%{_bindir}/pt-stalk
install -D -m 0755 $MBD/support-scripts/pt-summary $RBR/%{_bindir}/pt-summary
install -D -m 0755 $MBD/support-scripts/pt-table-checksum $RBR/%{_bindir}/pt-table-checksum
install -D -m 0755 $MBD/support-scripts/pt-table-sync $RBR/%{_bindir}/pt-table-sync
install -D -m 0755 $MBD/support-scripts/pt-table-usage $RBR/%{_bindir}/pt-table-usage
install -D -m 0755 $MBD/support-scripts/pt-upgrade $RBR/%{_bindir}/pt-upgrade
install -D -m 0755 $MBD/support-scripts/pt-variable-advisor $RBR/%{_bindir}/pt-variable-advisor
install -D -m 0755 $MBD/support-scripts/pt-visual-explain $RBR/%{_bindir}/pt-visual-explain


%files
%{_bindir}/CompressDbxBak
%{_bindir}/DatabaseBackup
%{_bindir}/NfsMount
%{_bindir}/RemoveDbxBak
%{_bindir}/SyncDBxBak
%{_bindir}/read_metadata
%{_bindir}/registe_metadata
#%doc



%changelog

