RPM_SOURCE_DIR=RPM/SOURCES

all: clean prep rpmbuild

prep:
	wget https://download.microsoft.com/download/f/c/d/fcd3f599-2d60-46c1-8628-45c2eff1b207/sqljdbc_8.4.1.0_enu.tar.gz -O sqljdbc.tar.gz
	tar -xzf sqljdbc.tar.gz
	mkdir -p ${RPM_SOURCE_DIR}
	cp sqljdbc_8.4/enu/mssql-jdbc-8.4.1.jre11.jar ${RPM_SOURCE_DIR}
	rm -rf sqljdbc.tar.gz sqljdbc_8.4

rpmbuild:
	rpmbuild -bb RPM/SPECS/artifactory-sqljdbc-jar.spec

clean:
	rm -rf ${RPM_SOURCE_DIR}