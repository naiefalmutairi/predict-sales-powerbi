import pandas as pd
from sklearn.linear_model import LinearRegression

# تحميل البيانات مع ترميز مناسب
df = pd.read_csv(r"C:\Users\DELL\Desktop\Power BI\sample sales data\sample sales data.csv", encoding='ISO-8859-1')
# تحويل عمود التاريخ إلى تنسيق تاريخ (اختياري فقط للعرض أو التحقق)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# استخدام MONTH_ID كمدخل للتنبؤ، وSALES كمخرجات
X = df[['MONTH_ID']]
y = df['SALES']

# بناء نموذج الانحدار الخطي
model = LinearRegression()
model.fit(X, y)

# التنبؤ بمبيعات الشهر القادم (رقم الشهر التالي)
next_month = pd.DataFrame({'MONTH_ID': [X['MONTH_ID'].max() + 1]})
prediction = model.predict(next_month)

# طباعة التوقع
print(f"توقع مبيعات الشهر القادم: {round(prediction[0], 2)} ريال")

# (اختياري) إضافة التوقعات على نفس الملف وحفظه
df['Predicted_Sales'] = model.predict(X)
# df.to_excel("Predicted_Sales.xlsx", index=False)
