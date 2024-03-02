grade:
	python3 grade.py

submit: ../p0-submission.zip

clean:
	rm -f test.db

../p0-submission.zip: load.sql 1.sql 2.sql 3.sql 4.sql 5.sql 6.sql 7.sql 8.sql
	zip $@ $^

../autograde.tar: Makefile data grade.py outputs schema.sql
	tar cf $@ $^ 

.PHONY: grade submit clean
