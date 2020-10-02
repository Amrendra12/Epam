import pandas
import sys

def student_marks(subject):
    df = pandas.read_csv(sys.argv[1])
    print("Mathematics marks of the top three students:  ")
    df.sort_values([subject], axis=0, ascending=[False], inplace=True)
    return df.head(3)

# We can get the value of top 3 marks based on the passed subject mentioned in the csv file ex: "maths", "science", "english", "physics", "chemistry" and "biology"
top_marks = student_marks("chemistry")
print(top_marks)
