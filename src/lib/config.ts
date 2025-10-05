export const OFFLINE = import.meta.env.VITE_OFFLINE === '1';
export const DATA_BASE = OFFLINE ? '/data' : '/data'; // force local
export const NOW_ISO = () => new Date().toISOString();
