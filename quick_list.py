#!/usr/bin/env python3
import subprocess
import json
import re

def get_transaction_info(tx_hash):
    dogecoin_cli = "/root/dogecoin-1.14.6/bin/dogecoin-cli"
    cmd = [dogecoin_cli, 'getrawtransaction', tx_hash, '1']  # '1' argument returns verbose transaction info
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    if result.stdout:
        tx_info = json.loads(result.stdout)
        return tx_info
    else:
        return None

def extract_and_decode_scriptsig(tx_info):
    if tx_info and 'vin' in tx_info and len(tx_info['vin']) > 0:
        vins = tx_info['vin']
        for vin in vins:
            if 'scriptSig' in vin and 'asm' in vin['scriptSig']:
                script_sig_asm = vin['scriptSig']['asm']
                return script_sig_asm

    return None

def extract_custom_section(script_sig_asm, target_string):
    start_index = script_sig_asm.find(target_string)
    if start_index != -1:
        end_index = start_index + len(target_string)
        return script_sig_asm[start_index:end_index]
    else:
        return None

def hex_to_text(hex_string):
    try:
        text = bytes.fromhex(hex_string).decode('utf-8')
        return text
    except UnicodeDecodeError:
        return "Cannot decode hex to text."

def parse_block_field(converted_text):
    match = re.search(r'"blk"\s*:\s*"([^"]+)"', converted_text)
    if match:
        return match.group(1)
    else:
        return None

if __name__ == "__main__":
    # Example transaction hash
    transaction_hash = "9368196c2482d0cde0b8431fd5ba15c2039999f4ddda02f57b4daa2c918a823c"
    
    # Get transaction information
    transaction_info = get_transaction_info(transaction_hash)

    # Extract and decode scriptSig
    script_sig_asm = extract_and_decode_scriptsig(transaction_info)

    if script_sig_asm:
        target_string = "7b2270223a22746170222c226f70223a22646d742d6d696e74222c22646570223a22616133613465346162313264346439303031383734366165326166623061356466653434363763666238393531306130393137343566336239333132363466306930222c227469636b223a226e6174646f6773222c22626c6b223a2235303230373939227d"
        extracted_section = extract_custom_section(script_sig_asm, target_string)

        if extracted_section:
            print("Original Hex String:", extracted_section)
            text_result = hex_to_text(extracted_section)
            print("Converted Text:", text_result)
            block_field = parse_block_field(text_result)
            if block_field:
                print("Parsed Block Field:", block_field)
            else:
                print("Block field not found.")
        else:
            print("Target string not found in ScriptSig (ASM).")
    else:
        print("ScriptSig extraction failed or no valid inputs found.")
