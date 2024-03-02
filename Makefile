submit: load.sql 1.sql 2.sql 3.sql 4.sql 5.sql 6.sql 7.sql 8.sql
	zip ../p0-submission.zip $^

clean:
	rm -f test.db
