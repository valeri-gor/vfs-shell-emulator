def test_simple_split():
    raw_input = "ls documents folder"
    
    parts = raw_input.split()
    
    assert parts[0] == "ls"
    assert parts[1:] == ["documents", "folder"]
