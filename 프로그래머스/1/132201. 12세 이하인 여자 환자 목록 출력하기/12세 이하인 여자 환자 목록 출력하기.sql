-- 코드를 입력하세요
SELECT PT_NAME,PT_NO, GEND_CD, AGE, IFNULL(TLNO,'NONE') AS TLNO from PATIENT WHERE age<=12 and GEND_CD = 'W' order by age DESC, PT_NAME