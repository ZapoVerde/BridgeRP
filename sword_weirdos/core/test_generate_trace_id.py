from ParetoDebug.adapters.debug_adapter import generate_trace_id

def test_generate_trace_id():
    tid = generate_trace_id()
    print(f"Generated trace ID: {tid}")

if __name__ == "__main__":
    test_generate_trace_id()
