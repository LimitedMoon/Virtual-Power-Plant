import random, math, json, datetime as dt

class DataAgent:
    def collect(self):
        h=dt.datetime.now().hour
        return {
            'hour': h,
            'load_kw': round(450+120*math.sin(h/24*6.28)+random.randint(-15,15),2),
            'temp_c': round(24+6*math.sin((h-6)/24*6.28),2),
            'price': 0.42 if 16<=h<=21 else 0.18,
            'battery_soc': round(random.uniform(0.3,0.95),2),
            'ev_count': random.randint(5,80)
        }

class ForecastAgent:
    def predict(self,data):
        vals=[]
        for i in range(1,7):
            drift=20*i if 16 <= (data['hour']+i)%24 <=21 else -6*i
            vals.append(round(data['load_kw']+drift+random.randint(-8,8),2))
        return vals

class StrategyAgent:
    def optimize(self,data,forecast):
        actions=[]; save=0
        if data['price']>0.3:
            actions.append('Shift HVAC to efficiency mode'); save+=40
        if max(forecast)>520 and data['battery_soc']>0.4:
            actions.append('Battery discharge for peak shaving'); save+=85
        if data['ev_count']>20:
            actions.append('Delay EV charging to valley pricing'); save+=35
        if not actions:
            actions=['Maintain baseline dispatch']
        return {
            'actions': actions,
            'peak_forecast_kw': max(forecast),
            'estimated_kw_reduction': save,
            'estimated_cost_saving_usd': round(save*data['price']/10,2)
        }

class ReportAgent:
    def render(self,data,forecast,plan):
        return json.dumps({
            'timestamp': str(dt.datetime.now()),
            'realtime': data,
            'forecast_next_6h': forecast,
            'dispatch_plan': plan,
            'summary': 'Enterprise AI token-intensive orchestration completed.'
        }, indent=2)
