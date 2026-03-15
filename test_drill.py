import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue

def test_clean_column():
    """Test that NaN values are filled with the median."""
    # إنشاء بيانات تجريبية (الوسيط هو 3.0)
    s = pd.Series([1, 2, np.nan, 4, 5])
    result = clean_column(s)
    
    # التأكد من عدم وجود قيم مفقودة ومطابقة النتيجة للوسيط
    assert result.isna().sum() == 0
    assert result[2] == 3.0

def test_compute_revenue():
    """Test that revenue is computed correctly."""
    # بيانات تجريبية للكمية والسعر
    q = pd.Series([10, 20])
    p = pd.Series([2, 5])
    result = compute_revenue(q, p)
    
    # النتيجة المتوقعة (10*2=20) و (20*5=100)
    expected = pd.Series([20, 100])
    pd.testing.assert_series_equal(result, expected)