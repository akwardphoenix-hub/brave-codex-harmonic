import { NOW_ISO } from './config';

export type AuditEntry = {
  ts: string;
  actor: string;
  action: string;
  refId?: string;
  meta?: Record<string, unknown>;
};

export function writeAuditLocal(entry: Omit<AuditEntry, 'ts'>) {
  const key = 'audit-log';
  const cur = JSON.parse(localStorage.getItem(key) || '[]');
  cur.push({ ts: NOW_ISO(), ...entry });
  localStorage.setItem(key, JSON.stringify(cur));
}

export function getAuditLocal(): AuditEntry[] {
  const key = 'audit-log';
  return JSON.parse(localStorage.getItem(key) || '[]');
}
