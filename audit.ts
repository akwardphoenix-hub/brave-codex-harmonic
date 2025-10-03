// src/utils/audit.ts
import { v4 as uuidv4 } from "uuid";

export interface AuditEntry {
  id: string;
  action: string;
  actor: string;
  timestamp: string;
  details: any;
}

export function createAuditEntry(
  action: string,
  actor: string,
  details: any = {}
): AuditEntry {
  return {
    id: uuidv4(),
    action,
    actor,
    timestamp: new Date().toISOString(),
    details,
  };
}
